using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
namespace Projetweb
{
    #region Stat
    public class Stat
    {
        #region Member Variables
        protected int _id;
        protected string _url;
        protected string _result;
        protected string _context;
        #endregion
        #region Constructors
        public Stat() { }
        public Stat(string url, string result, string context)
        {
            this._url=url;
            this._result=result;
            this._context=context;
        }
        #endregion
        #region Public Properties
        public virtual int Id
        {
            get {return _id;}
            set {_id=value;}
        }
        public virtual string Url
        {
            get {return _url;}
            set {_url=value;}
        }
        public virtual string Result
        {
            get {return _result;}
            set {_result=value;}
        }
        public virtual string Context
        {
            get {return _context;}
            set {_context=value;}
        }
        #endregion
    }
    #endregion
}