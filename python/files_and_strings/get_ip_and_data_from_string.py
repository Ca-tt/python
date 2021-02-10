# To-do
# Grab the ip adress from the sting
# and assign it to variable

string = 'Received: from nakamura.uits.iupui.edu (nakamura.uits.iupui.edu [134.68.220.122])'

ip_start_pos = string.find('[') + 1
print(ip_start_pos)

ip_end_pos = string.find(']', ip_start_pos)
print(ip_end_pos)

ip = string[ip_start_pos: ip_end_pos]
print(ip)

# To-do
# Grab the number after colon
# assign it to variable
# change type to float

data = 'X-DSPAM-Confidence: 0.8475'
num_start_pos = data.find(':') + 1
num_end_pos = len(data)
print(num_end_pos)

number = data[num_start_pos: num_end_pos]
result = float(number)
print('The result is:', result, type(result))
