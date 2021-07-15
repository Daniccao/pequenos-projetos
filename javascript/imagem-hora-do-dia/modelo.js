function carregar(){
    var msg = window.document.getElementById("msg")
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `Agora sao ${hora} horas!`

    //hora = 19 //hora para teste

    if(hora >= 4 && hora < 12){
        //Bom Dia
        img.src = 'foto_manha.png'
        document.body.style.background = '#f8db72'
    }
    else if(hora >= 12 && hora <= 17){
        //Boa Tarde
        img.src = 'foto_tarde.png'
        document.body.style.background = '#db6713'
    }
    else{
        //Boa Noite
        img.src = 'foto_noite.png'
        document.body.style.background = '#26273d'
    }
}
