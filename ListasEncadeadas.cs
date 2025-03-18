//Crição de nó.
//Estrutura criação de um nó simples.
class node
{ 
  private Object item;
  private Node prox;

  Node(Object item)
  {
      this.item = item;
      prox = null;
  }
}


//Inserir elementos em uma lista.
//Lista Simples, com os métodos insereInicio, insereFim, inserePosicao e contaNos.

public object primeiro { get; private set; }
public object ultimo { get; private set; }

class ListaSimples
{
    private Node primeiro, ultimo;
    private int qtdeNos;

    ListaSimples()
    {
        primeiro.setProx(null);
        ultimo.setProx(null);
    }
  void insereFim(Node novo)
    {
        novo.setProx(null);
        if (this.primeiro==null)
            this.primeiro = novo;
        if (this.ultimo != null)
            this.ultimo.setProx(novo);
        this.ultimo = novo;
    }
}
void insereInicio(Node novo)
{
        if (this.primeiro != null)
            novo.setProx(novo);
        else
        {
            if (this.primeiro == null)
                this.primeiro = novo;
            this.ultimo = novo;
        }
}
void inserePosicao(Node novo, int pos)
{
        Node aux = primeiro;
        int qtde = contaNos();
        int pos_aux;
        if(pos == 0)
        {
            novo.setProx(primeiro);
            if (primeiro == ultimo)
            {
                ultimo = novo;
            }
            primeiro = novo;
        }
        else
        {
            if(pos <= qtde)
            {
                pos_aux = 1;
                while(aux != null && pos > pos_aux)
                {
                    aux = aux.getProx();
                    pos_aux++;
                }
                aux.setProx(novo);
            }
            else
            {
                if(pos > qtde)
                {
                    ultimo.setProx(novo);
                    ultimo = novo;
                }
            }
        }
}
public int contaNos()
{
    int tam = 0;
    Node aux = primeiro;
    while (aux != null)
    {
        tam++;
      aux = aux.getProx();
    }
    return tam;
}


//Excluir elemento da lista.
//Método excluiNo da classe listaSimples.

void excluiNo (Object item)
{
    Node aux = primeiro;
    while (aux != null && aux.getItem()!=item)
    {
        aux = aux.getProx();
    }
    aux.setProx(aux.getProx().getProx());
    if (ultimo == aux.getProx())
        ultimo = aux;
}



//Buscar elemento em uma lista.
//Método buscaNo da classe listaSimples.

Node buscaNo(Object item)
{
    int i = 0;
    Node aux = primeiro;
    while (aux != null)
    {
        if(aux.getItem() == item)
        {
            return aux;
        }
        i++;
        aux = aux.getProx();
    }
    return null;
}



