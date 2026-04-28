const API="http://127.0.0.1:8000"


document
.getElementById(
'reservationForm'
)
.addEventListener(
'submit',
async function(e){

e.preventDefault()

const payload={
customer_name:
document.getElementById(
'name'
).value,

party_size:
parseInt(
document.getElementById(
'party'
).value
),

reservation_time:
document.getElementById('time').value + ":00"
}


await fetch(
`${API}/reservations/`,
{
method:'POST',
headers:{
'Content-Type':
'application/json'
},
body:JSON.stringify(payload)
}
)

alert("Reservation submitted")

})


async function loadReservations(){

const res=
await fetch(
`${API}/reservations/`
)

const data=
await res.json()

let html=''

data.forEach(r=>{
html+=
`<li>
${r.customer_name}
Party:${r.party_size}
</li>`
})

document
.getElementById(
'reservationList'
).innerHTML=html

}



async function loadDashboard(){

const res=
await fetch(
`${API}/analytics/dashboard`
)

const d=
await res.json()

document
.getElementById(
'dashboard'
).innerHTML=
`
<p>Reservations:
${d.today_reservations}</p>

<p>Occupancy:
${d.occupancy_rate}</p>

<p>Peak:
${d.peak_hour}</p>
`

}