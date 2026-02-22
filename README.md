# AWS S3 Backup Automation

This project automatically backs up files to an AWS S3 bucket using Python and a GitHub Actions CI/CD pipeline. The workflow can be scheduled using cron to perform automated backups.

## Features

* Upload files to AWS S3
* Automated backups using cron schedule
* CI/CD pipeline with GitHub Actions
* Simple and lightweight implementation

## Technologies Used

* Python (boto3)
* AWS S3
* GitHub Actions
* Linux

## Architecture

User → GitHub Repository → GitHub Actions → AWS S3 Bucket

## Prerequisites

* AWS Account
* IAM User with S3 permissions
* Python 3 installed
* Git installed

## Setup Instructions

1. Clone the repository

git clone https://github.com/your-username/repo-name.git

2. Install dependencies

pip install boto3

3. Configure AWS credentials (GitHub Secrets or local)

4. Run the script

python s3_backup.py

## CI/CD Workflow

The GitHub Actions workflow automatically runs the backup script based on the defined cron schedule or on push events.

## Future Improvements

* Add email notifications
* Support multiple file uploads
* Add logging and monitoring


## Author
Harsh
