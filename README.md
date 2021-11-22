# MM209Assignment
This project aims to find the pH20/pH2 ratio of 10 metal-metal oxide equilibriums at a temperature entered by the user.

Here the data values of the standard free energy change of the different metals have been collected from the website of University of Cambridge under it's Dissemination of IT for the Promotion of Materials Science (DoITPoMS) program,the link for which can be found here https://www.doitpoms.ac.uk/tlplib/ellingham_diagrams/interactive.php

The data values were compiled in the form of a excel sheet which was then converted to a csv file and fed into the code.

The calculations involve taking care of 2 simultaneous equilibriums.The first one being the formation of H20 in the form of 2H2 + O2 = 2H2O.The equilibrium constant for this reaction is calculated from the free energy values at the given temperature.Since the equilibrium constant is now known which is equal to ((pH2O/pH2)^2)/pO2 ,only the partial pressure of O2 is needed to calculate the required ratio

This partial pressure is found out by the metal-metal oxide equilibrium whose equilibrium constant is calculated from its free energy values at the specified temperature using the same procedure as above.Since the equilibrium constant is nothing but 1/pO2 the partial pressure is easily found out.Here we have assumed the activities of both the metal and the metal oxide are equal to 1 and there is a negligible difference.

One important consideration in the above process is the change in the slope of the free energy values due to melting/boiling of the metal or metal oxide.In the table of metals we are using only Magnesium shows a significant change in its free energy equation as the metal boils at 1365K.Hence the calculation depend on the temperature entered by the user.Although there are metal/metal oxide which melt in the temperature range 300K-1600K,their slopes remain largely unchanged and only magnesium shows a significant difference.

For running the code,the user needs to run the iPython notebook and enter the temperature value.The output contains a data frame which contains the free energy value,metal-metal oxide equilibrium constant,pO2 and pH2O/pH2 values for each of the metals.A bar graph is drawn to also visualise the obtained values.In addition the user can also add metals of their own choice to the data frame uncommenting the code provided in one of the initial cells and adding the required values.The code is reusable and should work for other metals as well
