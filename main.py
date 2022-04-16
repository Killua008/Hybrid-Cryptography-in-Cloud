from tkinter import*
from tkinter import messagebox
import os
import boto3
from botocore.exceptions import ClientError
from PIL import Image
import smtplib
import imghdr
from email.message import EmailMessage
import hybrid1




#upload
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    messagebox.showinfo("Information","Upload Completed!")
    return True




