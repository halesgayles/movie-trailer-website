(function () {
    $(document).ready(function () {

        var triggers = $('.button');

        for (var i = 0; i < triggers.length; i++) {


            $('#myModal' + i).on('hidden.bs.modal', function (index) {
                return function () {
                    /* when modal is hidden, set original src link to blank and
                    then set it back to the duplicated src link so next click on button
                    returns trailer instead of blank modal
                     */
                    var dupSrc = $('#myFrame' + index).attr('src');
                    $('#myFrame' + index).attr('src', '');
                    $('#myFrame' + index).attr('src', dupSrc);

                }
            }(i));


        }


    });

})();

