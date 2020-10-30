from dns import resolver

# IP address of google.com
result = resolver.query('google.com', 'A')
print('*'*150)
for ipval in result:
    print('IP', ipval.to_text())
    print('*'*150)

# A CNAME record also known as Canonical Name Record is a type of 
# record in the Domain Name System (DNS) used to map a domain name as an alias for another domain.
result = resolver.query('mail.google.com', 'CNAME')
print('*'*150)
for cnameval in result:
    print('cname target address:', cnameval.target)
    print('*'*150)