from PyRouge.pyrouge import Rouge

r = Rouge()
fptr1 = open('test.eval_titles.txt')
fptr2 = open('eval_articles.1_300000.txt')
system_summaries = fptr1.readlines()#.split()
model_summaries = fptr2.readlines()#.split()
avg_p= avg_r=avg_f1=0
for i in range(len(system_summaries)):
    [precision, recall, f_score] = r.rouge_l([system_summaries[i]], [model_summaries[i]])
    avg_p += precision
    avg_r += recall
    avg_f1 += f_score
    
    print("Sentence:",i)
    print("Human:",system_summaries[i])
    print("Model:",model_summaries[i])
    print("Precision is :"+str(precision)+"\nRecall is :"+str(recall)+"\nF Score is :"+str(f_score))
    print()

print("----------------------Final eval-------------------")
print("Precision:",(float)(avg_p/len(system_summaries)))
print("Recall:",(float)(avg_r/len(system_summaries)))
print("F1-score:",(float)(avg_f1/len(system_summaries)))
