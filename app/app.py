import gradio as gr
import pandas as pd
import joblib

# unknown_types = sio.get_untrusted_types(file="Model/credit_loan_detection.skops")
pipe = joblib.load("fraud_detection_model.joblib")
def predict_credit_risk(step, amount, oldbalanceOrig, oldbalanceDest, isMerchantDest, countOrig, type):

    amount = amount // 1000
    oldbalanceOrig = oldbalanceOrig // 1_000
    oldbalanceDest = oldbalanceDest // 1_000
    match(isMerchantDest): # Kredit/KPR : 0, Lainnya : 1, Pribadi: 2, Menyewa : 3
        case "Customer":
            isMerchantDest = 0
        case _: # Merchant
            isMerchantDest = 1
    
    match(type):
        case "Setor":
            type = 0
        case "Tarik":
            type = 2
        case "Debit":
            type = 0
        case "Pembayaran":
            type = 1
        case _: # Transfer
            type = 2

    features = [step, amount, oldbalanceOrig, oldbalanceDest, isMerchantDest, countOrig, type]
    
    features = [features]
    prediction = pipe.predict(features)[0]

    label = f"Status Transaksi: {'Fraud' if prediction == 1 else 'Aman'}"

    try:
        df1 = pd.read_csv('dataset.csv')
        df2 = pd.DataFrame({
            "step":[step],
            "amount":[amount],
            "oldbalanceOrig":[oldbalanceOrig],
            "oldbalanceDest":[oldbalanceDest],
            "isMerchantDest":[isMerchantDest],
            "countOrig":[countOrig],
            "type":[type],
            'isFraud':[prediction]
        })
        pd.concat([df1, df2], axis=0).to_csv("dataset.csv", index=False)
    except:
        pd.DataFrame({
            "step":[step],
            "amount":[amount],
            "oldbalanceOrig":[oldbalanceOrig],
            "oldbalanceDest":[oldbalanceDest],
            "isMerchantDest":[isMerchantDest],
            "countOrig":[countOrig],
            "type":[type],
            'isFraud':[prediction]
        }).to_csv("dataset.csv", index=False)

    return label

inputs = [
    gr.Number(minimum=1, label="step"), #step
    gr.Number(minimum=1_000, label="Jumlah Transfer (Rp)"), #amount
    gr.Number(minimum=1_000, label="Isi saldo pengirim (Rp)"), #oldbalanceOrig
    gr.Number(minimum=1_000, label="Isi saldo penerima (Rp)"), #oldbalanceDest
    gr.Dropdown(choices=["Customer", "Merchant"], label="Status penerima"), #isMerchantDest
    gr.Number(minimum=1, label="Jumlah transfer dilakukan nasabah"), #countOrig
    gr.Dropdown(choices=['Setor', 'Tarik', 'Debit', 'Pembayaran', 'Transfer'], label='Jenis transaksi'), # type

]

outputs = [gr.Label(num_top_classes=1, label="Hasil Prediksi")]

examples = [
    [9.00, 2482740_000.91, 21309_000.00, 645110_000.66,'Customer',1.00, 'Pembayaran'],
    [5.00, 281593_000.55, 2085292_000.46, 2772312_000.14, 'Merchant', 1.00, 'Debit'],
    [7.00, 262434_000.54, 262434_000.54, 19525_000.79, 'Customer', 1.00, 'Transfer'],
    [8.0, 222_000.0, 222_000.0, 1_000, "Customer", 1.0, "Tarik"]
]

title = "Financial Fraud Detection"
description = "Aplikasi ini mengklasifikasi apakah transaksi untuk tujuan penipuan atau tidak."
article = "Anggota Kelompok: " \
"\n- Andrew Salim (205150207111048)" \
"\n- Ryan Satrio Pamungkas (205150207111046)" \
"\n- Jaya Winata (225150200111038)"
"\n\nAplikasi ini menggunakan model machine learning untuk klasifikasi transaksi fraud."

gr.Interface(
    fn=predict_credit_risk,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
).launch()
