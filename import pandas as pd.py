import pandas as pd

# Assume 'df' is your existing GuardDuty dataframe and 'threat_intel' is loaded from CSV
threat_intel = pd.read_csv('threat_intel.csv')

# 1. Left merge to enrich the GuardDuty logs with threat intelligence
df = df.merge(
    threat_intel, 
    how='left', 
    left_on='attacker_ip', 
    right_on='ip_address'
)

# 2. Fill the NaN values for IPs that didn't match the threat feed
df['threat_actor_group'] = df['threat_actor_group'].fillna('Unknown Actor')
df['malware_family'] = df['malware_family'].fillna('Unknown')

# Drop the redundant 'ip_address' column brought over from the CSV
df = df.drop(columns=['ip_address'])

print(df[['type', 'attacker_ip', 'threat_actor_group']].head())