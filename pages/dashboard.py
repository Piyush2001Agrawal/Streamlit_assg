import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.title("This is Diwali Sales Data page")
st.markdown("This is the Dashboard page of the where the Diwali sales analysis is done.")
df= pd.read_csv("Preprocessed_Diwali_sales", encoding='unicode_escape')
st.subheader("Diwali Sales Data")
st.dataframe(df)

gender = st.sidebar.multiselect('Gender',
                                options=df['Gender'].unique(),
                                default=df['Gender'].unique())

filtered_df =df[
    (df['Gender'].isin(gender))]

fig= px.bar(filtered_df,x='Gender', y='Amount', color='Product_Category', barmode='group',
       title='Total Amount by Gender')
st.plotly_chart(fig)
st.markdown("This bar graph shows the Total amount spend on Product by Gender")

fig1 =  px.bar(df, x='Age Group', y='Orders', color='Age Group', 
       title='Total Orders by Age Group')
st.plotly_chart(fig1)
st.markdown("This bar graph shows the Total Number of Orders by Age Group")

top_states = df.groupby('State')['Amount'].sum().nlargest(10).reset_index()
fig2= px.bar(top_states, x='State', y='Amount', color='State', 
             title='Top 10 States by Total Amount',template='plotly_dark')
st.plotly_chart(fig2)
st.markdown("This bar graph shows the Top 10 States by Total Amount")

fig3= px.sunburst(filtered_df, path=['Gender', 'Age Group'], values='Amount', 
             title='Amount by Gender and Age Group',template='plotly_dark')
st.plotly_chart(fig3)
st.markdown("This sunburst graph shows the Gender and Age Group wise Amount spend on Product")

fig4= px.imshow(df[['Orders', 'Amount', 'Age']].corr(), text_auto=True, 
          title='Correlation Heatmap',template='plotly_dark',
          color_continuous_scale='YlGnBu')
st.plotly_chart(fig4)
st.markdown("This heatmap shows the correlation between Orders, Amount and Age")

fig5= px.funnel(df.groupby('Age Group')['Amount'].sum().reset_index(), x='Amount', y='Age Group',
                title='Funnel Chart of Amount by Age Group', template='plotly_dark')
st.plotly_chart(fig5)
st.markdown("This funnel chart shows the Amount spend by Age Group")

fig6= px.treemap(df, path=['State', 'Product_Category'], values='Orders',
           title='Treemap of Orders by State and Product Category',template='plotly_dark')
st.plotly_chart(fig6)
st.markdown("This treemap shows the Orders by State and Product Category")

fig7= px.scatter(df, x='Age', y='Orders', size='Amount', color='Zone',
                 title='Bubble Chart: Orders vs Age (Bubble Size = Amount)',
                 hover_data=['State', 'Product_Category'])
st.plotly_chart(fig7)
st.markdown("This bubble chart shows the Orders vs Age with Bubble Size as Amount and colored by Zone")

fig8= px.line(filtered_df, x='Gender',y ='Orders', markers='o',
        title='Total Orders by Gender',template='plotly_dark',color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig8)
st.markdown("Line chart show total orders by gender")

fig9=px.pie(filtered_df, names='Gender',
       title='Gender Distribution',template='plotly_dark',)
st.plotly_chart(fig9)
st.markdown("This Pie chart show the gender distribution")

fig10= px.violin(df, x='Product_Category', y='Orders', color='Product_Category',
       title='Total Orders by Product Category',template='plotly_dark',
       color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig10)
st.markdown("This violin chart shows the Total Orders by Product Category")

 