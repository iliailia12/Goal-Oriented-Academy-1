'''20)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგი, ამ სტრინგზე გამოიყენეთ find()
 ფუნქცია და თუ find ფუნქცია დააბრუნებს ლუწ ინდექს მაშინ ეს სტრინგი დააბრუნეთ 
 დიდი ასოებით (upper) ხოლო თუ დააბრუნებს კენტ ინდექსს, მაშინ დააბრუნეთ ეს სტრინგ
 ი რომლის პირველი ასოც
 იქნება დიდი (capitalize)'''

def average(numbers_list):
    
    return sum(numbers_list) / len(numbers_list)
numbers = [1, 5, 12]
print(average(numbers))

