#!/usr/bin/env python
# coding: utf-8

# # Código Python para geração de orçamentos em PDF

# In[2]:


print("Orçamento gerado com sucesso")


# # Entrada de Dados

# In[6]:


input ("Digite a descrição do projeto: ")
input ("Digite o total de horas estimadas: ")
input ("Digite o valor da hora trabalhada: ")
input ("Digite o prazo estimado: ")


# # Gravação de Dados

# In[16]:


Projeto = input ("Digite a descrição do projeto: ")
Horas_Estimadas = input ("Digite o total de horas estimadas: ")
Valor_Hora = input ("Digite o valor da hora trabalhada: ")
Prazo_Estimado = input ("Digite o prazo estimado: ")


# In[17]:


print (Projeto)
print (Horas_Estimadas)
print (Valor_Hora)
print (Prazo_Estimado)


# # Cálculos

# In[18]:


Total_Estimado = int(Horas_Estimadas) * int(Valor_Hora)


# In[21]:


print(Total_Estimado)


# # Gerador de PDF

# In[23]:


get_ipython().system('pip install fpdf')


# In[29]:


from fpdf import FPDF


# In[36]:


pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0)


pdf.text(115, 145, Projeto)
pdf.text(115, 160, Horas_Estimadas)
pdf.text(115, 175, Valor_Hora)
pdf.text(115, 190, Prazo_Estimado)
pdf.text(115, 205, str(Total_Estimado))
pdf.output("Orçamento.pdf")
print("Orçamento Gerado com Sucesso")


# In[ ]:




