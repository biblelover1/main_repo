Console.WriteLine("Size");
int size = Convert.ToInt32(Console.ReadLine());
string [] newArray = {"arfd", "der", "dfw", "fdf"};
string [] array = Create3symbArray(newArray);
ShowArray(array);


string [] Create3symbArray(string [] newArray)
{
    
    int count = 0;
    for(int i = 0; i < newArray.Length; i++)
    {
        string a = newArray[i];
        if(a.Length <=3) count++; 
    }
    string [] symb3Array = new string[count];
    for(int i = 0, j = 0; i < newArray.Length; i++)
    {
        string a = newArray[i];
        if(a.Length<=3)
        {
            symb3Array[j] = newArray[i];
            j++;
        }
    }
    return symb3Array;
}

void ShowArray(string [] showArr)
{
    for(int i=0; i<showArr.Length; i++)
    {
        Console.Write($"{showArr[i]} ");
    }
}