(function () {
    $(document).ready(function () {

        var triggers = $('.button');

        for (var i = 0; i < triggers.length; i++) {

            $('#myModal' + i).on('hidden.bs.modal', function (index) {
                return function (e) {
                    var dupSrc = $('#myFrame' + index).attr('src');
                    $('#myFrame' + index).attr('src', '');
                    $('#myFrame' + index).attr('src', dupSrc);

                }
            }(i));


        }


    });

})();

