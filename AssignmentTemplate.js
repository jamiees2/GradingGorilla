// grades are mandatory
var grades = /*grades*/;
// comments are optional
/*comments*/

var form = document.forms.namedItem("Form2");

for (var kt in grades)
{
    console.log('Setting grade: '+kt)
    var grade = form.elements.namedItem("grade"+kt);
    if(grade == null) {
        console.error("WARN: " + kt + " did not exist! Did he bail??");
        continue;
    }
    grade.value = grades[kt];
    if (typeof(comments) != 'undefined' && kt in comments)
    {
        var memo = form.elements.namedItem("memo"+kt);
        memo.value = comments[kt];
    }
}
