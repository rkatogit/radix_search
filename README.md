# SUMMARY
Script for check if a prefix in iplist matches IOC in Threatlist

python3.x

# Usage
```
python radix-search-ip.py iplist TS_Threatlist
```

iplist format example  
```
1.1.1.1/32  
2.2.2.0/24  
3.3.0.0/16  
```

if you want csv output, change last line to like below, 

df.query('IOC == %s' % matchlist).to_csv('result.csv',index=False)

