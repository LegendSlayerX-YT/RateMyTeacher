const name_elmt = document.getElementById('School Name');
const state_elmt = document.getElementById('School State');
const city_elmt = document.getElementById('School City');
const zip_code_elmt = document.getElementById('School Zip Code');
const address_elmt = document.getElementById('School Address');
const grade_levels_elmt = document.getElementById('School Grade Levels');
const button_elmt = document.getElementById('Search School');
const school_list_elmt = document.getElementById('school_list');

const add_name_elmt = document.getElementById('Add School Name');
const add_state_elmt = document.getElementById('Add School State');
const add_city_elmt = document.getElementById('Add School City');
const add_zip_code_elmt = document.getElementById('Add School Zip Code');
const add_address_elmt = document.getElementById('Add School Address');
const add_grade_levels_elmt = document.getElementById('Add School Grade Levels');
const add_button_elmt = document.getElementById('Add School');
const cancel_add_button_elmt = document.getElementById('Cancel Add School');


button_elmt.addEventListener('click', handleSearch);

async function handleSearch() {
    school_list_elmt.innerHTML = ''
    const name = name_elmt.value;
    const state = state_elmt.value;
    const city = city_elmt.value;
    const zip_code = zip_code_elmt.value;
    const address = address_elmt.value;
    const grade_levels = grade_levels_elmt.value;
    const response = await fetch('/school/query?' + new URLSearchParams({
        name: name,
        state: state,
        city: city,
        zip_code: zip_code,
        address: address,
        grade_level: grade_levels,
    }));
    const data = await response.text();
    const parsed = JSON.parse(data);
    for (let i = 0; i < parsed.length; i++) {
        const newDiv = document.createElement("button");
        newDiv.innerHTML = `${parsed[i].name ?? ''}
        <br> ${parsed[i].state ?? ''} 
        <br> ${parsed[i].city ?? ''}
        <br> ${parsed[i].zip_code ?? ''}
        <br> ${parsed[i].address ?? ''}
        <br> ${parsed[i].grade_level ?? ''}`
        newDiv.id = 'School Id_' + parsed[i].id;
        newDiv.addEventListener('click', handleSchoolClick);
        school_list_elmt.appendChild(newDiv);
    }
    const add_school_button = document.createElement("button");
    add_school_button.innerHTML = 'Add a School';
    school_list_elmt.appendChild(add_school_button);
    add_school_button.addEventListener('click', handleAddSchoolButton);
}

function handleAddSchoolButton() {
    const add_school_div = document.getElementById("add_school_params")
    add_school_div.classList.remove('hidden')
    add_name_elmt.value = name_elmt.value;
    add_state_elmt.value = state_elmt.value;
    add_city_elmt.value = city_elmt.value;
    add_zip_code_elmt.value = zip_code_elmt.value;
    add_address_elmt.value = address_elmt.value;
    add_grade_levels_elmt.value = grade_levels_elmt.value;
}

add_button_elmt.addEventListener('click', handleActuallyAddSchool)
async function handleActuallyAddSchool() {
    const name = add_name_elmt.value;
    const state = add_state_elmt.value;
    const city = add_city_elmt.value;
    const zip_code = add_zip_code_elmt.value;
    const address = add_address_elmt.value;
    const grade_levels = add_grade_levels_elmt.value;
    const response = await fetch('/school/add?' + new URLSearchParams({
        name: name,
        state: state,
        city: city,
        zip_code: zip_code,
        address: address,
        grade_level: grade_levels,
    }));
    const data = await response.text();
    const parsed = JSON.parse(data);
    if(parsed.school_id){
        alert('School add success');
        const add_school_div = document.getElementById("add_school_params");
        add_school_div.classList.add('hidden');
        name_elmt.value = add_name_elmt.value;
        state_elmt.value = add_state_elmt.value;
        city_elmt.value = add_city_elmt.value;
        zip_code_elmt.value = add_zip_code_elmt.value;
        address_elmt.value = add_address_elmt.value;
        grade_levels_elmt.value = add_grade_levels_elmt.value;
        handleSearch();
    }
    else{
        alert('School add failure ' + parsed.error);
    }
}

cancel_add_button_elmt.addEventListener('click', handleCancelAdd)
function handleCancelAdd() {
    const add_school_div = document.getElementById("add_school_params")
    add_school_div.classList.add('hidden')
}


function handleSchoolClick(event){
    const clicked_button = event.target;
    const id = clicked_button.id;
    school_id = id.slice('School Id_'.length);
    window.location.href = `/teacher?school_id=${school_id}`;
}