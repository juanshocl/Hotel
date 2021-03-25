
$(function () {


    $('.btnAddClient').on('click', function () {
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('hidden.bs.modal', function (e) {
        $('#frmClients').trigger('reset');
    });

    // event submit
    $('#frmClients').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'addCli');
        submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de crear este cliente?', parameters, function (response) {
                // console.log(parameters);
                // var newOption = new Option(response.cliente, false, true);
                // $('select[name="SelectBookingClientId"]').append(newOption).trigger('change');
                $('#myModalClient').modal('hide');
                location.reload();
            });
    });



    // $('#frmClients').on('submit', function (e) {
    //     e.preventDefault();
    //     var parameters = $(this).serializeArray();
    //     $.ajax({
    //         url: window.location.pathname,
    //         type: 'POST',
    //         data: parameters,
    //         dataType: 'json',
    //     }).done(function (data) {
    //         if(!data.hasOwnProperty('error')){
    //             return false;
    //         }
    //     }).fail(function (jqXHR, textStatus, errorThrown) {
    //         //alert(textStatus + ': ' + errorThrown);
    //     }).always(function (data) {
           
    //     });
        

    // });

    $('#frmBooking').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        parameters.append('action', 'add');
        submit_with_ajax(window.location.pathname, 'Notificación',
        '¿Estas seguro de crear este cliente?', parameters, function (response) {
            location.href = '/booking/';
            });
    });
    //     var parameters = $(this).serializeArray();
    //     $.ajax({
    //         url: window.location.pathname,
    //         type: 'POST',
    //         data: parameters,
    //         dataType: 'json',
    //     }).done(function (data) {
    //         if(!data.hasOwnProperty('error')){

    //             return false;
    //         }
    //     }).fail(function (jqXHR, textStatus, errorThrown) {
    //         //alert(textStatus + ': ' + errorThrown);
    //     }).always(function (data) {
           
    //     });
        

});
