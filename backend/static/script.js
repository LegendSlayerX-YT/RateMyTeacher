
const name_elmt = document.getElementById('Teacher Name');
const email_elmt = document.getElementById('Teacher Email');
const button_elmt = document.getElementById('Search')
const teacher_list_elmt = document.getElementById('teacher_list')

async function handleInput() {
    const name = name_elmt.value;
    const email = email_elmt.value;
    const response = await fetch(`/teacher/query?teacher_name=${String(name)}&teacher_email=${String(email)}`);
    const data = await response.text();
    const parsed = JSON.parse(data);
    for (let i = 0; i < parsed.length; i++) {
        const newDiv = document.createElement("input");
        newDiv.type='button';
        newDiv.value=`${parsed[i].name} \n ${parsed[i].email}`
        teacher_list_elmt.appendChild(newDiv);
    } 
}


button_elmt.addEventListener('click', handleInput);
