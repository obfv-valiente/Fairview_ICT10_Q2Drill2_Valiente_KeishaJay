from pyscript import display, document

def add_brand(e):
    document.getElementById('output1').innerHTML =""
    grade7 = {'Uniqlo','Bench','Zara'}
    #students = {'Uniqlo','Bench','Zara'}


input_student= document.getElementById('input1').value

new_student_set = {input_brand}
#new_student = LN + "" + FN

all_students = students | new_student_set

total_students = len( students | new_student_set)

student_list = "<br>".join(sorted(all_students))

#display
document.getElementById('output1').innerHTML = f'All brands: <br> {student_list}'
display(f'Total brands: {total_students}', "target='output1" )