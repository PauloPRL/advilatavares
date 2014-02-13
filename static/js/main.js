/**
 * Created by carlos on 01/02/14.
 */
$(function(){
    $('#id_mobile_phone').mask('(99) 99999-9999?9');

    $('#id_phone, #id_commercial_phone').mask('(99) 9999-9999');

    $('#id_birthday').mask('99/99/9999');

    $('#id_cpf').mask('999.999.999-99');

    $('#form-members').submit(function(evt){
        var birth = $('#id_birthday').val();
        var cpf = $('#id_cpf').val();
        var rg = $('#id_rg').val();

        if(birth.length){
            year = birth.split('/').pop();
            year_old = new Date().getFullYear() - parseInt(year);

            if(year_old >= 18 && cpf.length == 0){
                alert('Preencha o Campo CPF');
                return false;
            }

            if(year_old >= 18 && rg.length == 0){
                alert('Preencha o Campo RG');
                return false;
            }
        }else{
            alert('Preencha a Data de Nascimento');
            return false;
        }

        return true;
    });

    $('.carousel').carousel({
        interval: 5000
    });
	$.mask.load = function(){};
	$.mask.close = function(){}
});
