#!usr/bin/bash
aws s3 ls adminsbucketfromcli
aws s3 cp ./testFileTOUpload.txt s3://adminsbucketfromcli/
aws s3 ls adminsbucketfromcli