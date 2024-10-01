import streamlit as st
import pandas as pd
# import base64


# def display_pdf(file_path):
#     with open(file_path, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'''
#     <style>
#     iframe {{
#         width: 100%;
#         height: 100vh;
#     }}
#     </style>
#     <iframe src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
#     '''
#     st.markdown(pdf_display, unsafe_allow_html=True)

class pages():
    
    def home(self):
        st.title("Rag, Tin, and Roll Designs")
        st.caption('3D Prints')
        
        # tab1, tab2= st.tabs(["Quantifind Website", "Why Quantifind"])
        # with tab1:
        #     st.header('Quantifind UI')
        #     url = "https://www.quantifind.com/"
        #     st.caption("Quantifind Documentation Found Here [NIPR Website](%s)" % url)
        #     st.image('modules/media/QF Webpage.png', width=800)
            
        # with tab2:
        #     st.header('Why Quantifind')
        #     url2 = "https://www.quantifind.com/why-quantifind/"
        #     st.caption("Why Quantifind [NIPR Website](%s)" % url2)
        #     raph = 'rcoelho@kpler.com'
        #     henr = 'hgoulart@kpler.com'
        #     st.caption(f'Kpler MarineTraffic POC: Raphael Coelho ({raph}) & Henrique Goulart ({henr})')
        #     st.subheader('Kpler MarineTraffic UI')
            # st.image('modules/media/Why_QF.png', width=900)
        
        # st.write("Quantifind uncovers hidden signals of risk associated with people and organizations from billions of open-source data points to help analysts increase the speed, accuracy, and coverage of their investigations.")
        # st.write("Quantifind’s AI platform, GraphyteTM has been battle-tested with banks and intelligence agencies, leveraging over a decade of R&D. It combines entity resolution, risk modeling, and relationship extraction into highly flexible outputs for easy integration into critical workflows.")
        # file_path = "modules/media/Quantifind Capability Statement 2024.pdf"
    
        # Provide a download link for the PDF
        # b64 = base64.b64encode(open(file_path, 'rb').read()).decode()  # decode base64 encoded file
        # download_link = f'<a href="data:application/octet-stream;base64,{b64}" download="Quantifind_Capability_Statement_2024.pdf">Download PDF</a>'
        # st.markdown(download_link, unsafe_allow_html=True)
        # display_pdf(file_path)
    
    def prints(self):
        st.header('3d Prints')
        # st.write("""Quantifind’s SaaS solutions are powered by a comprehensive set of external data sources. Access to these sources, through 
        # the Quantifind platform, is generally included in the Quantifind subscription. Quantifind sources these data in raw form through a 
        # variety of means including bulk license agreements, pay-per-search APIs, and web scraping. Note this data is exclusively public data 
        # or derived from public data.""")

        # st.write("""The data 200+ sets available in the Quantifind Graphyte Knowledge Graph include Unstructured Data, 
        #     Corporate Data, US Sanctions and Watchlists, International Sanctions and Watchlists, Politically Exposed Persons Database, 
        #     ICIJ Bahamas Leaks, ICIJ Offshore Leaks, ICIJ Panama Papers, ICIJ Paradise Papers, News Archives, Open Corporates, Foreign News 
        #     Archives, and Panjiva (International Shipping and Trade Data). There are also seven Risk Factors which are models/topics applied 
        #     to news articles and structured data sets. These Risk Factors include General, National Security, Crimes - General, Crimes - 
        #     Financial, Crimes - Environmental Social Governance, Financial Health, and High Risk Industry. For more information on these 
        #     data sets and risk factors see the first document shown below.""")

        # st.write("""Quantifind is continuously identifying and integrating new data sources into its services. When a new source is added, 
        # all customers benefit immediately. Customers also always have the option to subset the data sources accessed, depending on preference 
        # or use case, through the use of configuration parameters. A detailed list of the data sources is provided in the second document shown below.""")

        # file_path2 = "modules/media/Graphyte Platform_ Data Sets and Risks.pdf"
        # file_path3 = "modules/media/Appendix IV Quantifind Data Sources (2024-07).pdf"

        # st.divider()

        # b64_3 = base64.b64encode(open(file_path3, 'rb').read()).decode()  
        # download_link = f'<a href="data:application/octet-stream;base64,{b64_3}" download="Graphyte Platform_ Data Sets and Risks.pdf">Download PDF</a>'
        # st.markdown(download_link, unsafe_allow_html=True)
        # display_pdf(file_path2)

        # st.divider()

        # b64_2 = base64.b64encode(open(file_path2, 'rb').read()).decode()  
        # download_link = f'<a href="data:application/octet-stream;base64,{b64_2}" download="Quantifind_Capability_Statement_2024.pdf">Download PDF</a>'
        # st.markdown(download_link, unsafe_allow_html=True)
        # display_pdf(file_path3)


    def future_page(self):
        st.title('Future Page')
        # st.write("This is a sample of the product available from Quantifind.")
        # st.write("""Alexei Borisovich Miller is a prominent Russian businessman with close personal ties to Vladimir Putin. In 2001, Putin appointed 
        # Miller to the position of CEO of GAZPROM, Russia's largest energy producer. Below is an image, relationship diagram, and Quantifind report on Miller.""")

        # st.divider()
        # col1, col2 = st.columns(2)
        # with col1:
        #     with st.popover("Alexei Borisovich Miller Photo"):
        #         st.image("modules/media/abm_mugshot.png", width=400, use_column_width=False)
        # # st.image("modules/media/abm_mugshot.png", width=400, use_column_width=False)
        # # st.write("Alexei Borisovich Miller")

        # with col2:
        #     with st.popover("Connection to Vladamir Putin"):
        #         st.image("modules/media/accomplice.png", width=600, use_column_width=False)
        # # st.image("modules/media/accomplice.png")
        # file_path4 = "modules/media/QF-response-ABM-html.pdf"

        # st.divider()

        # data = pd.read_csv('modules/media/QF.csv')
        # search_query = st.text_input("Keyword Search", "")
        # if search_query:
        #     data = data[data['Name'].str.contains(search_query, case=False, na=False) |
        #                 data['Source'].str.contains(search_query, case=False, na=False) |
        #                 data['Source Description'].str.contains(search_query, case=False, na=False) |
        #                 data['Note'].str.contains(search_query, case=False, na=False)]

        # selectedRiskLevel = st.selectbox('Select Risk Level:', ['All'] + list(data['Risk Level'].unique()))
        # if selectedRiskLevel != 'All':
        #     data = data[data['Risk Level'] == selectedRiskLevel]
        # st.write(data)
        # st.divider()
        # b64_4 = base64.b64encode(open(file_path4, 'rb').read()).decode()  
        # download_link = f'<a href="data:application/octet-stream;base64,{b64_4}" download="QF-response-ABM-html.pdf">Download PDF</a>'
        # st.markdown(download_link, unsafe_allow_html=True)

        # display_pdf(file_path4)

    def page_info(self):
        st.title("Page Information")
        # st.markdown(
        #     """
        #     Quantifind REST APIs are application programming interfaces (API) that support search against Quantifind’s proprietary 
        #     risk assessment service. Given the name - and potentially other metadata - corresponding to a person or organization, 
        #     this service identifies risk based on information in the public domain and as available through a number of proprietary 
        #     Data Sources. Quantifind’s APIs enable automation in anti-financial crime (AFC) use cases including:

        #     *   Know Your Customer (KYC)/Customer Due Diligence
        #     *   Name Screening
        #     *   Alerts Triage
        #     *   Investigations
        #     *   Continuous Monitoring

        #     Quantifind’s APIs are accessed over the Internet and securely routes search traffic to Quantifind’s private cloud where 
        #     its proprietary technology is deployed. These APIs requires no on-premise software installation and is designed with data 
        #     security and data privacy as critical features.
        #     """
        # )

        # st.divider()
        # st.write("Using the UI manually to search for entities.")
        # st.image('modules/media/api_results0.png', width=800)

        # st.divider()

        # file_path5 = "modules/media/Graphyte Resource Center.pdf"
        # b64_5 = base64.b64encode(open(file_path5, 'rb').read()).decode()  
        # download_link = f'<a href="data:application/octet-stream;base64,{b64_5}" download="Graphyte Resource Center.pdf">Download PDF</a>'
        # st.write("Graphyte Resource Center and API Documentation.")
        # st.markdown(download_link, unsafe_allow_html=True)
        # display_pdf(file_path5)

    def about(self):
        st.title("About")
        # st.write("IDST Contacts")
        # s_email = "anthony.w.sweet.civ@socom.mil"
        # g_email = "gary.b.graham.civ@socom.mil"
        # st.write('For more information or accesss to the Quantifind Data source, please contact:')
        # st.write(f"Anthony Sweet: {s_email} | Gary Graham: {g_email}")

if __name__ == "__main__":
    app_pages = pages()
    app_pages.home()