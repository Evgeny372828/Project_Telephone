const bur= document.getElementById('bur')
const menu= document.getElementById('menu')
const close=document.getElementById('close')
bur.addEventListener('click',function open() {
  if (bur.style.display ==="flex") {
    bur.style.display="none"
    menu.style.display="flex"
  }
  else {
    bur.style.display = "flex";
    menu.style.display="none"
  }
})
close.addEventListener('click',function open() {
  if (close.style.display ==="flex") {
    close.style.display="none"
    menu.style.display="none"
    bur.style.display="flex"
  }
  else {
    close.style.display = "flex";
    menu.style.display="flex"
  }
})