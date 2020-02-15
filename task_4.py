
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


x = np.linspace(-np.pi, np.pi, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.sin(x*2))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()

