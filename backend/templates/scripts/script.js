
const name_elmt = document.getElementById('Teacher Name');
const email_elmt = document.getElementById('Teacher Email');
const button_elmt = document.getElementById('Search')

async function handleInput() {
    const name = name_elmt.value;
    const email = email_elmt.value;
    const response = await fetch(`/teacher/query?teacher_name=${String(name)}&teacher_email=${String(email)}`);
    const data = await response.json();
    const parsed = JSON.parse(data);
    for (let i = 0; i < data.length; i++) {
        const newDiv = document.createElement("div");
        newDiv.textContent = parsed[i].name;
        newDiv.textContent = parsed[i].email;
        document.body.appendChild(newDiv);
    } 
}


button_elmt.addEventListener('click', handleInput);
