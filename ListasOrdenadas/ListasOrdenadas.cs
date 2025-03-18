//Método de inserção em uma lista ordenada encadeada.

void insereNoOrdenado(Node novo)
{
  Node aux;
  //Verificando se a lista está vazia
  if (primeiro == null || contaNos() == 0)
  {
      novo.setProx(primeiro);
      primeiro = novo;
  }
  else
  {
      aux = primeiro;
      int valorNovo = Convert.ToInt32(novo.getItem());
      int valorAux = Convert.ToInt32(aux.getItem());
      while (aux.getProx() != null && valorNovo > valorAux)
      {
          aux = aux.getProx();
      }
      novo.setProx(aux.getProx());
      aux.setProx(novo);
  }
}

