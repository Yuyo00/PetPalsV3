$(document).ready(function() {

  $.get('https://fakestoreapi.com/products',

    function(registros){

      setTimeout(`
          $('#imagen-de-espera').hide();
          $('#pagina-concurso').show();
        `, 1000);

      var premioHTML = $('#premio').prop('outerHTML');
      premioHTML = premioHTML.replace('d-none', '');

      $('#lista').empty();

      $.each(registros, function(i, item) { 
          recuadro = premioHTML;
          recuadro = recuadro.replace('src=""', `src="${item.image}"`);
          recuadro = recuadro.replace('[[nombre]]', item.title);
          recuadro = recuadro.replace('[[precio]]', item.price);
          recuadro = recuadro.replace('[[descripcion]]', item.description);
        
        $('#lista').append(recuadro);
      
    });

  });

});