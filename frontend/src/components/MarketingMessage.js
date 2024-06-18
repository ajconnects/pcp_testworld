import React from 'react';
import { MDBRow, MDBCol } from 'mdb-react-ui-kit';
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

function MarketingMessage() {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1
  };

  const slides = [
    {
      title: "How work should work",
      text: "Forget the old rules. You can have the best people. Right now. Right here.",
      image: "https://www.careergirls.org/wp-content/uploads/2015/06/Computer_Programmer1920X10180.jpg"
    },
    {
      title: "Another great headline",
      text: "Find the best talent for your projects in just a few clicks.",
      image: "https://usa.bootcampcdn.com/wp-content/uploads/sites/106/2021/03/CDG_blog_post_image_02-850x412.jpg"
    },
    {
      title: "Work efficiently",
      text: "Optimize your workflow with the best tools available.",
      image: "https://cdn3.f-cdn.com/files/download/97941784/programmin.jpg"
    },
    {
      title: "Collaboration at its best",
      text: "Work with teams across the globe seamlessly.",
      image: "https://kazokku.com/blog/wp-content/uploads/2023/06/apa-itu-programmer.webp"
    }
  ];

  return (
    <div className="marketing-message">
      <Slider {...settings}>
        {slides.map((slide, index) => (
          <div key={index}>
            <MDBRow>
              <MDBCol size="md-6">
                <h2 className="title">{slide.title}</h2>
                <p className="text">{slide.text}</p>
              </MDBCol>
              <MDBCol size="md-6" className="image-container">
                <img src={slide.image} alt={slide.title} className="uploaded-image" />
              </MDBCol>
            </MDBRow>
          </div>
        ))}
      </Slider>
    </div>
  );
}

export default MarketingMessage;