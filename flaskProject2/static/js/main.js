const btnDelete = document.querySelectorAll('.btb-delete')

if(btnDelete){
   const btnArray= Array.from(btnDelete);
   btnArray.forEach((btn)=> {
btn.addEventListener('click',(e)=>{
   if(!confirm('Seguro de que deceas eliminar este contacto?')){
      e.preventDefault();
   }
  });
});
}