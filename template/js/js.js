function habilita_botao(){

    var quantidade = document.getElementsByClassName('btn btn-danger');
    
    for (var i = 0;i < quantidade.length; i++){ 
        
        var status = document.getElementsByClassName('status')[i].innerHTML;
        if (status.trim() == 'Fechado'){
          document.getElementsByClassName('btn btn-danger')[i].disabled = true;
        }
    }
  }
  
  
  
  function myFunction() {
      alert("Salvo com sucesso");
    }
  
  