import pandas as pd
import datetime
import smtplib
import os



def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")


if __name__ == "__main__":
    # just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "your message", item['Dialogue'])
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        # print(df.loc[i, 'Year'])

    # print(df)
    df.to_excel('data.xlsx', index=False)

    print(df)
