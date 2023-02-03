$("#btn").on('click', function () {
    console.log($('.email').html())
    var email = $("#emailModer").val();
    if (isEmail(email) && email !== '') {
        $(this).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Создается ТКС ')
    }
})

function makeCounter() {
    var currentCount = 1;
    return function () {
        return currentCount++;
    }
}

var counter = makeCounter();

$("#addModer").on('click', function () {
    var count = counter()
    $("#add_moder").append(
        '<input type="email" class="form-control" id="" name="moder' + count + '" aria-describedby="emailHelp" placeholder="name@example.com" value="' + count + '@qwert.qwer.ru" required><div id="emailHelp" class="form-text">Введите email внутреней почты</div>'
    )
})

function isEmail(email) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2})+$/;
    return regex.test(email);
}

$(".col").on('click', function () {
        if ($(this).text().length === 47) {
            $(this).parent('.card').attr('class', 'card border-danger')
            $(this).prev('.card-body').children('.stream').attr('class', 'stream card-tex text-danger text-center').text('stream on IVR')
            $(this).children('.btn').text('cutter Off').attr('class', 'btn btn-danger ')

        } else {
            console.log($("#btnCutter").text())
            $(this).prev('.card-body').children('.stream').attr('class', 'stream card-tex text-center').text('stream on AVAYA')
            $(this).parent('.card').attr('class', 'card')
            $(this).children('.btn').text('cutter On').attr('class', 'btn btn-primary ')
        }
    }
)

var button = $('.btn').length
console.log(button)