$(document).ready(function(){

    let carImage = "#carImage";
    let carName = "#carName";
    let carYear = "#carYear";
    let carType = "#carType";
    let carMileage = "#carMileage";
    let bookButton = "#bookButton";

    $.ajax({
        type: 'GET',
        url: 'localhost:5000/api',
        success: function(carOrder){
            $.each(carOrder, function(i, carOrder){
                $(carImage).attr('src', carOrder[i].carImage);
                $(carName).html(carOrder[i].carName);
                $(carYear).html(carOrder[i].carYear);
                $(carType).html(carOrder[i].carType);
                $(carMileage).html(carOrder[i].carMileage);
                $(bookButton).attr('href', carOrder[i].bookButton);
                $(bookButton).html(`NGN ${carOrder[i].carPrice}/Day`)
            });
        }, error: function(){
            alert('error loading cars')
        }
    });
});
