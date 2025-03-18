//Árvores binárias
//Classe que cria a estrutura de nó da árvore.

Class BTreeNo
{
      private int valor;
      private BTreeNo esq;
      private BTreeNo dir;

      BTreeNo(int valor)
      {
          this.valor = valor;
      }
      public void setValor(int valor)
      public void setEsc(BTreeNo esq)
      public void setDir(BTreeNo dir)
      public int getValor()
      public BTreeNo getEsc()
      public BTreeNo getDir()
}



//Inserir nó em uma árvore

//Classe que cria a estrutura de nó da àrvore

Class BTree
{
      private BTreeNo raiz;

      private BTreeNo inserir(BTreeNo arvore, int novo)
      {
            BTreeNo aux = null;
            if (arvore == null)
            {
                  aux.setValor(novo);
                  return aux;
            }
            else if (novo < arvore.getValor())
                  arvore.setEsq(inserir(arvore.getEsq(), novo));
            else
                  arvore.setDir(inserir(arvore.getDir(), novo));

            return arvore;
      }
      public void inserirNo(int novo)
      {
            raiz = inserir(raiz novo);
      }
}
