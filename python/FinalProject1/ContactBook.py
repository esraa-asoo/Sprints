import csv
import os
import boto3
import pathlib
import pandas as pd
from datetime import datetime
from os import path
now = datetime.now()

def Menu():
    options = input(
        "please choose:"
        "\n1: Add a new contact "
        "\n2: Update contact"
        "\n3: Delete contact"
        "\n4: View contact"
        "\n5: Backup contact"
        "\n6: quit\n")
    if options == '1':
        AddRecord()
    elif options == '2':
        update()
    elif options == '3':
        delete()
    elif options == '4':
        view_file()
    elif options == '5':
        aws_backup()
    elif options == '6':
        print("*** Have a nice day ***")
        return 1
    else:
        print("Enter one of the options ")
    print("*" * 30)
    Menu()


#AddRecord is a function to add the contact information(insertion time, name, address, phone number, and email address)

def AddRecord():
    # receive the fields from user
    name = input("Enter the name: ")
    address = input("Enter the home address: ")
    email = input("Enter the email: ")
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    phone = str(input("Enter the phone number: "))

    data = [name, address, email, phone, date]
    Save(data)
# This Function create today file if not exist , append if exist then save the argument data in it

def update():
    SelectedFile = input("Enter the file name you want to edit: ")
    if not path.exists(SelectedFile):
        print("the file is not exist, try again")
        return 1
    df = pd.read_csv(SelectedFile)
    name = input("Enter the name you want to edit: ")
    rowindex = ''
    for idx, row in df.iterrows():
        if row['Name'] == name:
            rowindex = idx
            print(rowindex)
    if rowindex == '':
        print("Name is not found!!")
        return 1
        # updating the contacts
    edit_part = input("change to edit-->\n1:name\n2:address\n3:email address\n4:phone\n")
    if edit_part == '1':
        name = input("Enter the new name: ")
        df.iloc[rowindex, 0] = name
        df.to_csv(SelectedFile, index=False)
    elif edit_part == '2':
        address = input("Enter the new address: ")
        df.iloc[rowindex, 1] = address
        df.to_csv(SelectedFile, index=False)
    elif edit_part == '3':
        email = input("Enter the new email address: ")
        df.iloc[rowindex, 2] = email
        df.to_csv(SelectedFile, index=False)
    elif edit_part == '4':
        phone = input("Enter the new phone: ")
        df.iloc[rowindex, 3] = phone
        df.to_csv(SelectedFile, index=False)
    print("The file has been updated successfully ")

    # This Function to allow the user to  choose file and delete any record in it by using its name
def delete():
        SelectedFile = input("Enter the file name you want to delete from: ")
        # check the file is exist or not
        if not path.exists(SelectedFile):
            print("the file is not found, try again")
            return 1
        df = pd.read_csv(SelectedFile)
        name = input("Enter the name you want to delete it: ")
        for idx, row in df.iterrows():
            if row['Name'] == name:
                rowindex = idx
                df = df.drop(df.index[rowindex])
                print("successfully deleted")
                df.to_csv(SelectedFile, index=False)
                return 1
        print("Not founded!!!")
# This Function to allow the user to  choose file to view its content
def view_file():
    SelectedFile = input("Enter the file name to view: ")
    if not path.exists(SelectedFile):
        print("The file is not found, try again")
        return 1
    with open(SelectedFile, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

# This Function copy all files in a folder and archive it ,then uploaded the archive file to s3 bucket
def aws_backup():
    # check if folder is exist
    if not path.exists("aws_backup"):
        os.system("mkdir aws_backup")
    # copy all csv files in it and then archive the folder
    os.system("copy  *.csv aws_backup")
    os.system("tar -cvzf  aws_backup_zip aws_backup")
    print("Welcome to aws")
    # Take the s3 bucket name iam credentials to allow uploading to s3
    access_Key = input("please insert your iam aws access key: ")
    secret_Key = input("please insert your iam aws secret key: ")
    bucket_name = input("please input the bucket name: ")
    s3 = boto3.client("s3", aws_access_key_id=access_Key, aws_secret_access_key=secret_Key)
    object_name = "aws_backup_zip"
    file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "aws_backup_zip")
    response = s3.upload_file(file_name, bucket_name, object_name)

def Save(data):
    filename = "contactbook_" + now.strftime("%d-%m-%Y") + ".csv"
    with open(filename, 'a+', newline='\n') as file:
        writer = csv.writer(file)
        # check if the file is empty so it write the headers
        if os.stat(filename).st_size == 0:
            writer.writerow(["Name", "Home address", "Email Address", "Phone Number", "Date"])
        # save the data in the file
        writer.writerow(data)
