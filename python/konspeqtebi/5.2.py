# boolean expressions

# boolean - მონაცემთა ტიპი, აქვს ორი მნიშვნელობა True/False

# შემდგომი მაგალითები იყენებენ ოპერატორ ==, რომელიც ადარებს ორ მონაცემს და თუ ისინი ერთმანეთის ტოლია აბრუნებს True ბულეან მნიშვნელობას, თუ ერთმანეთს არ უდრის აბრუნებს False ბულეან მნიშვნელობას

# მაგ:

print(5 == 5)
# True

print(5 == 6)
# False

# True და False არაა სტრინგ მონაცემთა ტიპი ის ეკუთვნის ბულეან მნიშვნელობას. ამის გასაგებად ჩვენ უბრალოდ შეგვიძლია გამოვიყენოთ აწ უკვე ნასწავლი type ფუნქცია

print(type(True))

# <class 'bool'>

print(type(False))

# <class 'bool'>

# == ოპერატორი ეთერთი relation operators მათგანია, ამის გარდა კიდევ გვაქვს:

x = 10
y = 20

x != y # x არ უდრის y
x > y # x მეტია y
x < y # x ნაკლებია y
x >= y # x მეტია ან ტოლია y
x <= y # x ნაკლებია ან ტოლია y


# შესაძლოა ეს მათემატიკური ოპერაციები შენთვის ნაცნობია მაგრამ სინტაქსი ოდნავ განსხვავდება. მაგ: = ნაცვლად პითონში არის ==, და არ არსებობს =< ან =>. ტოლობა იწერება ყოველთვოს მარჯვნივ.

