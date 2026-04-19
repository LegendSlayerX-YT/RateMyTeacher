const name_elmt = document.getElementById('Teacher Name');
const email_elmt = document.getElementById('Teacher Email');
const button_elmt = document.getElementById('Search')
const teacher_list_elmt = document.getElementById('teacher_list')
const school_info_div = document.getElementById('School Info')

async function onWindowLoad() {
    if (SCHOOL_ID_FROM_LOAD == null){
        return
    }
    const response = await fetch('/school/query?' + new URLSearchParams({
        id: SCHOOL_ID_FROM_LOAD,
    }));
    const data = await response.text();
    const parsed = JSON.parse(data);
    if (parsed.length>0){
        const newDiv = document.createElement("div");
        newDiv.innerHTML = `${parsed[0].name ?? ''}
        <br> ${parsed[0].state ?? ''} 
        <br> ${parsed[0].city ?? ''}
        <br> ${parsed[0].zip_code ?? ''}
        <br> ${parsed[0].address ?? ''}
        <br> ${parsed[0].grade_level ?? ''}`
        school_info_div.appendChild(newDiv);
    }
}

async function handleInput() {
    const name = name_elmt.value;
    const email = email_elmt.value;
    const response = await fetch('/teacher/query?' + new URLSearchParams({
        teacher_name: name,
        teacher_email: email,
        school_id: SCHOOL_ID_FROM_LOAD ?? '',
    }));
    const data = await response.text();
    const parsed = JSON.parse(data);
    for (let i = 0; i < parsed.length; i++) {
        const newDiv = document.createElement("button");
        newDiv.innerHTML = `${parsed[i].name} <br> ${parsed[i].email}`
        teacher_list_elmt.appendChild(newDiv);
    } 
}


button_elmt.addEventListener('click', handleInput);
