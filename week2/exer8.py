emails_list_tup = []
for k,v in emails.items():
    emails_list_tup.append((v,k))

print(sorted(emails_list_tup))

email_count, email_count_max = sorted(emails_list_tup, reverse=True)[1] #or -1
print()



## incomplete solution!!!
