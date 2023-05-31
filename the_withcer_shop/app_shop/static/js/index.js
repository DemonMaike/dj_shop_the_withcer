const listNav = document.querySelectorAll('.nav-item');
const current = document.querySelector('.active');
for (let i=0; i<listNav.length; i++){
  listNav[i].addEventListener('click', ()=>{
    current.classList.remove('active');
    listNav[i].classList.add('active');
  })
}
