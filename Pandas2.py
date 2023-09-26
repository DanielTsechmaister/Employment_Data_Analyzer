import pandas as pd
import numpy as np

class Data_Analyzer():
    def __init__(self,fname):
        self.df = pd.read_csv(fname)

    def __repr__(self):
        return repr(self.df.head())

    # Q1
    def omit_zeros(self,colnames):
        self.df.replace(np.NAN, 0, inplace=True)
        self.df = self.df[(self.df[colnames] != 0).all(axis=1)]

    # Q2
    def calc_total(self, col1, col2, newcol):
        def f(df):
            new = df[col1] + (df[col1] * df[col2]/100)
            return new

        self.df[newcol] = self.df.apply(f, axis=1)

    # Q3
    def select_group(self, group_col, group):
        gro = self.df.groupby(group_col)
        return gro.get_group(group)

    # Q4
    def summ_by_group(self, d, group_cols,val_col,funcs):
        gro = d.groupby(group_cols)
        return gro[val_col].agg(funcs)


    # Q5
    def concat_dfs(self, dfs=list, col1="", col2="", newcol="diff"):
        df_n = pd.concat(dfs, axis=1)
        df_n.columns = [col1,col2]
        df_n[newcol] = df_n[col1] - df_n[col2]
        df_n = df_n.reset_index()

        return df_n

    # Q6
    def merge(self, left, right, col="diff"):
        df = pd.DataFrame()
        i_left, i_right = 0, 0
        while i_left < left.shape[0] and i_right < right.shape[0]:
            if left[col].iloc[i_left] < right[col].iloc[i_right]:
                df = pd.concat([df, left.iloc[[i_left]]], ignore_index=True)
                i_left += 1
            else:
                df = pd.concat([df, right.iloc[[i_right]]], ignore_index=True)
                i_right += 1
        while i_left < left.shape[0]:
            df =  pd.concat([df, left.iloc[[i_left]]], ignore_index=True)
            i_left += 1
        while i_right < right.shape[0]:
            df = pd.concat([df, right.iloc[[i_right]]], ignore_index=True)
            i_right += 1
        return df



    def merge_sort(self, L, col="diff"):
        if L.shape[0] <= 1:
            return L
        mid = L.shape[0]//2
        left = self.merge_sort(L[:mid] ,col)
        right = self.merge_sort(L[mid:],col)

        return self.merge(left, right, col)




def main():
    data = Data_Analyzer('employment.csv')
    print(data)

    # Q1
    data.omit_zeros(colnames = ["Gender", "Salary","Bonus %"])
    print(sum(data.df["Gender"]==0))
    print(sum(data.df["Salary"]==0))
    print(sum(data.df["Bonus %"]==0))

    # Q2
    data.calc_total("Salary", "Bonus %", "total")
    print(data)
    print(np.all(np.round((data.df.loc[:,"Salary"]*(1+(data.df.loc[:,"Bonus %"]/100))),1)==np.round(data.df.loc[:,"total"],1)))

    # Q3
    females_salaries = data.select_group(group_col = "Gender", group = "Female")
    males_salaries = data.select_group(group_col="Gender", group="Male")
    print(females_salaries.shape)
    print(males_salaries.shape)

    # Q4
    females_salaries = data.summ_by_group(females_salaries,group_cols = ["Team"],val_col = ["total"],funcs = [np.mean])
    print(females_salaries.shape)
    print(females_salaries)
    males_salaries = data.summ_by_group(males_salaries,group_cols = ["Team"],val_col = ["total"],funcs = [np.mean])
    print(males_salaries.shape)
    print(males_salaries)

    #Q5
    join_dfs = data.concat_dfs([females_salaries, males_salaries],col1="females",col2="males",newcol = "diff")
    print(join_dfs.shape)
    print(join_dfs)

    # Q6
    arr = data.merge_sort(join_dfs,"diff").reset_index(drop=True)
    print(arr)

if __name__=="__main__":
    main()
