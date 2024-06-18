import React from 'react';
import { MDBContainer, MDBRow, MDBCol } from 'mdb-react-ui-kit';
import { FaCode, FaMobileAlt, FaCloud, FaDatabase, FaRobot, FaPalette } from 'react-icons/fa';

function Categories() {
  const categories = [
    { 
      id: 1, 
      name: "Development and IT", 
      buttonText: ["JavaScript", "Python", "Java", "C#", "C++"].join(", "), 
      icon: <FaCode /> 
    },
    { 
      id: 2, 
      name: "AI Services", 
      buttonText: ["Python", "Java", "R", "Scala"].join(", "), 
      icon: <FaRobot /> 
    },
    { 
      id: 3, 
      name: "Design and Creative", 
      buttonText: ["Photoshop", "Illustrator", "InDesign"].join(", "), 
      icon: <FaPalette /> 
    },
    { 
      id: 4, 
      name: "Mobile Development", 
      buttonText: ["Swift", "React Native", "Flutter"].join(", "), 
      icon: <FaMobileAlt /> 
    },
    { 
      id: 5, 
      name: "Cloud Computing", 
      buttonText: ["AWS", "Google Cloud", "IBM Cloud"].join(", "), 
      icon: <FaCloud /> 
    },
    { 
      id: 6, 
      name: "Data Science", 
      buttonText: ["Python", "R", "SQL", "Scala"].join(", "), 
      icon: <FaDatabase /> 
    },
  ];

  const handleCategoryClick = (category) => {
    console.log(`Category ${category.name} clicked`);
    // Here you can handle navigation to another page if necessary.
  };

  return (
    <MDBContainer className="categories-container">
      <h2 className="categories-title">Find talent by category</h2>
      <MDBRow className="category-row">
        {categories.map(category => (
          <MDBCol key={category.id} size="md-4">
            <div className="category-button" onClick={() => handleCategoryClick(category)}>
              <div className="category-icon">{category.icon}</div>
              <div className="category-info">
                <h3>{category.name}</h3>
                <p>{category.buttonText}</p>
              </div>
            </div>
          </MDBCol>
        ))}
      </MDBRow>
    </MDBContainer>
  );
}

export default Categories;