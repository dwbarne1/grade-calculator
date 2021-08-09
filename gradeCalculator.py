import os

finalGrade = 0

categoriesAndPoints = {'Exercise' : {'Points Earned' : 0.00, 'Total Points' : 160, 'Weight' : 3, 'Grade' : 0.00},
                       'Assignment' : {'Points Earned' : 0.00, 'Total Points' : 210, 'Weight' : 10, 'Grade' : 0.00},
                       'Project' : {'Points Earned' : 0.00, 'Total Points' : 100, 'Weight' : 17, 'Grade' : 0.00},
                       'Quiz' : {'Points Earned' : 0.00, 'Total Points' : 80, 'Weight' : 25, 'Grade' : 0.00},
                       'Exam' : {'Points Earned' : 0.00, 'Total Points' : 200, 'Weight' : 36, 'Grade' : 0.00},
                       'Final' : {'Points Earned' : 0.00, 'Total Points' : 100, 'Weight' : 9, 'Grade' : 0.00}
                       }

print('Add together all points earned for each grade category\n'
      '(Hint: Do not add your lowest score for the 3 categories with a dropped score):\n')

for key in categoriesAndPoints:
    categoriesAndPoints[key]['Points Earned'] = float(input(f'Enter total points earned for {key}: '))
    categoriesAndPoints[key]['Grade'] = (categoriesAndPoints[key]['Points Earned'] / categoriesAndPoints[key]['Total Points']) * categoriesAndPoints[key]['Weight']
    finalGrade += categoriesAndPoints[key]['Grade']

print('\nGrade Information:\n')

print('Category     | Pts Earned | Total Points | Weight | Grade |')
print('-----------------------------------------------------------')
print(f'Exercise     |       {categoriesAndPoints["Exercise"]["Points Earned"]}|        {categoriesAndPoints["Exercise"]["Total Points"]}     | {categoriesAndPoints["Exercise"]["Weight"]}  | {round(categoriesAndPoints["Exercise"]["Grade"], 2)}')
print(f'Assignment   |       {categoriesAndPoints["Assignment"]["Points Earned"]}|        {categoriesAndPoints["Assignment"]["Total Points"]}     | {categoriesAndPoints["Assignment"]["Weight"]} | {round(categoriesAndPoints["Assignment"]["Grade"], 2)}')
print(f'Project      |       {categoriesAndPoints["Project"]["Points Earned"]}|        {categoriesAndPoints["Project"]["Total Points"]}     | {categoriesAndPoints["Project"]["Weight"]} | {round(categoriesAndPoints["Project"]["Grade"], 2)}')
print(f'Quiz         |       {categoriesAndPoints["Quiz"]["Points Earned"]}|        {categoriesAndPoints["Quiz"]["Total Points"]}      | {categoriesAndPoints["Quiz"]["Weight"]} | {round(categoriesAndPoints["Quiz"]["Grade"], 2)}')
print(f'Exam         |       {categoriesAndPoints["Exam"]["Points Earned"]}|        {categoriesAndPoints["Exam"]["Total Points"]}     | {categoriesAndPoints["Exam"]["Weight"]} | {round(categoriesAndPoints["Exam"]["Grade"], 2)}')
print(f'Final        |       {categoriesAndPoints["Final"]["Points Earned"]}|        {categoriesAndPoints["Final"]["Total Points"]}     | {categoriesAndPoints["Final"]["Weight"]}  | {round(categoriesAndPoints["Final"]["Grade"], 2)}')

print(f'\nFinal Grade: {round(finalGrade, 2)}')
