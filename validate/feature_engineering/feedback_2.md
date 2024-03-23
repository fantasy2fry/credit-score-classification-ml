- PyOD - can you add some explanation as to why you predict 4% will be outliers?
(contamination = 0.04 if I understand correctly, we set this ourselves based on prediction)
- Maybe outliers will be more clearly visible on boxplots? Than on scatterplots (idk)
- For SVC, you can use the classification_report(y_val, y_pred) function and the results will be nicely visible together, generally for every model it's worth calling this function, it's a nice and clear summary. Especially in the case of SVC, it's easy to get lost in what is what
- Cool idea with the chart comparing individual results, it increases readability :)
- Maybe try to check if omitting some columns will improve the results
- It would be nice to add some concluding remarks summarizing which options are the best and why