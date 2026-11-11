# Cloud Security Intelligence Data Pipeline

This repository contains an end-to-end data analytics architecture designed to ingest, process, and visualize cloud security telemetry (AWS CloudTrail & GuardDuty). 

**Executive Summary:**
* **Infrastructure & FinOps:** Designed a highly cost-efficient, serverless data lake using **Terraform** to provision immutable **S3** storage, enabling "schema on-read" log querying via **AWS Athena** to eliminate idle database compute costs.
* **Data Engineering & Threat Hunting:** Engineered automated threat intelligence pipelines in **Python**, leveraging vectorized **Pandas** operations to parse nested JSON logs, perform anomaly detection, and enrich incidents with known malicious IP datasets.
* **Executive Visibility:** Modeled massive security telemetry into a highly performant **Star Schema**, utilizing **DAX** to build dynamic **Power BI** dashboards that filter millions of rows in milliseconds to track critical threat actor KPIs.