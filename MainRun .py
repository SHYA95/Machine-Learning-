{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c9cf38b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in Tkinter callback\n",
      "Traceback (most recent call last):\n",
      "  File \"/Users/shroukyasser/opt/anaconda3/lib/python3.9/tkinter/__init__.py\", line 1892, in __call__\n",
      "    return self.func(*args)\n",
      "  File \"/var/folders/xd/m_59h85n2bx9btpq93blxlyh0000gn/T/ipykernel_4212/3375333742.py\", line 35, in Best_Class\n",
      "    os.startfile(r\"C:\\Users\\MAHE\\Downloads\\Tkinter_Module\\final_project\\models\\Best_Classifier.py\",operation=\"open\")\n",
      "AttributeError: module 'os' has no attribute 'startfile'\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import tkinter as tk\n",
    "from tkinter import *\n",
    "import sys, subprocess\n",
    "\n",
    "\n",
    "root= Tk()\n",
    "root.title('Main runner')\n",
    "root.geometry('800x450')\n",
    "#root.configure(fg=)\n",
    "\n",
    "\n",
    "def KNC():\n",
    "    os.startfile(r\"F:\\Tkinter_Module\\final_project\\models\\KNC.py\",operation=\"open\")\n",
    "\n",
    "def KNN():\n",
    "    os.startfile(r\"F:\\Tkinter_Module\\final_project\\models\\NaiveBayes.py\",operation=\"open\")\n",
    "\n",
    "def SVMCls():\n",
    "    os.startfile(r\"F:\\Tkinter_Module\\final_project\\models\\SVM-Clas.py\",operation=\"open\")\n",
    "\n",
    "\n",
    "def LinReg():\n",
    "    os.startfile(r\"F:\\Tkinter_Module\\final_project\\models\\LinearReg.py\",operation=\"open\")\n",
    "\n",
    "def LogReg():\n",
    "    os.startfile(r\"F:\\Tkinter_Module\\final_project\\models\\LogisticReg.py\",operation=\"open\")\n",
    "\n",
    "def DecCls():\n",
    "    opener = \"open\" if sys.platform == \"darwin\" else \"xdg-open\"\n",
    "    subprocess.call([opener, \"/Users/shroukyasser/Desktop/MLPROJECT/Decision - Cls.py.ipynb\"])\n",
    " \n",
    "    \n",
    "def Best_Class():\n",
    "    os.startfile(r\"C:\\Users\\MAHE\\Downloads\\Tkinter_Module\\final_project\\models\\Best_Classifier.py\",operation=\"open\")\n",
    "\n",
    "def Best_Reg():\n",
    "    os.startfile(r\"C:\\Users\\MAHE\\Downloads\\Tkinter_Module\\final_project\\models\\Best_Regressor.py\",operation=\"open\")\n",
    "    \n",
    "\n",
    "Label(root,text=\"Choose the model based on the type of problem\",font=\"System\").place(x=200,y=20) \n",
    "\n",
    "\n",
    "Label(root,text=\"Regression\",font=\"System\").place(x=150,y=75)\n",
    "Label(root,text=\"Classification\",font=\"System\").place(x=550,y=75)\n",
    "\n",
    "\n",
    "Button(root,text='K-Neighbors',activebackground=\"black\",command=KNC,activeforeground=\"white\").place(x=550,y=220)\n",
    "Button(root,text='KNN',command=KNN,activebackground=\"black\",activeforeground=\"white\").place(x=550,y=160)\n",
    "#Button(root,text='Multinomial Naive-Bayes',activebackground=\"black\",command=NBCls,activeforeground=\"white\").place(x=550,y=220)\n",
    "Button(root,text='SVM Classifier',activebackground=\"black\",command=SVMCls,activeforeground=\"white\").place(x=550,y=130)\n",
    "#Button(root,text='SVM Regressor',activebackground=\"black\",command=SVMReg,activeforeground=\"white\").place(x=150,y=220)\n",
    "#Button(root,text='Lasso Regression',activebackground=\"black\",command=Lasso,activeforeground=\"white\").place(x=150,y=190)\n",
    "#Button(root,text='Ridge Regression',activebackground=\"black\",command=Ridge,activeforeground=\"white\").place(x=150,y=160)\n",
    "Button(root,text='Linear Regression',activebackground=\"black\",command=LinReg,activeforeground=\"white\").place(x=150,y=130)\n",
    "#Button(root,text='Logistic Regression',activebackground=\"black\",command=LogReg,activeforeground=\"white\").place(x=550,y=250)\n",
    "# Button(root,text='MLP Classifier',activebackground=\"black\",command=MLPCls,activeforeground=\"white\").place(x=550,y=160)\n",
    "#Button(root,text='DecisionTree Regressor',activebackground=\"black\",command=DecReg,activeforeground=\"white\").place(x=150,y=250)\n",
    "Button(root,text='DecisionTree Classifier',activebackground=\"black\",command=DecCls,activeforeground=\"white\").place(x=550,y=190)\n",
    "\n",
    "Label(root,text= \"Best Classifier and Regressor  \",font=\"System\").place(x=250,y=350)\n",
    "\n",
    "Button(root,text='Best Classifier',activebackground=\"black\",command=Best_Class,activeforeground=\"white\").place(x=250,y=390)\n",
    "Button(root,text='Best Regressor',activebackground=\"black\",command=Best_Reg,activeforeground=\"white\").place(x=400,y=390)\n",
    "\n",
    "root.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd37b963",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7946ca6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4f0e399",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
