# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя
# делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

sum_num = int(input('Сумма чисел, которые загадал Петя: '))
product_num = int(input('Произведение чисел, которые загадал Петя: '))
first_num = 0
second_num = 0
for first_num in range (sum_num):
  second_num = sum_num - first_num
#  print (first_num, second_num)
  if first_num * second_num == product_num:
    break
if first_num * second_num == product_num:
  print (f"Петя задумал числа {first_num} и {second_num}")
else:  
  print (f"При заданной сумме и произведению загаданных Петей, не существует решения задачи")