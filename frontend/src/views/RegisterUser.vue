<template>
    <div>
        <form  @submit.prevent="handleSubmit" class="register-form">
            <div class="form-group">
                <table>Nama Lengkap:</table>
                <input type="text">
            </div>
            <div class="form-group">
                <table>Email:</table>
                <input type="email">
            </div>
            <div class="form-group">
                <table>Username:</table>
                <input type="text">
            </div>
            <div class="form-group">
                <table>Password</table>
                <input type="password">
            </div>
            <button>
                register
            </button>
        </form>
    </div>
</template>

<script>
export default{
    data(){
        return{
            form:{
                nama:'',
                email:'',
                username:'',
                password:''
            },
            errors:{}
        }
    },
    methods:{
        validateForm(){
            this.errors ={}

            if(!this.form.nama){
                this.errors.nama = 'nama dibutuhkan'
            }else if(!this.isValidnama(this.form.nama)){
                this.errors.nama = 'nama tidak valid'
            }

            if(!this.form.email){
                this.errors.email = 'Email dibutuhkan'
            }else if(!this.isValidEmail(this.form.email)){
                this.errors.email = 'Email tidak valid'
            }

            if(!this.form.username){
                this.errors.username = 'username dibutuhkan'
            }else if(!this.isValidusername(this.form.username)){
                this.errors.username = 'username tidak valid'
            }

            if(!this.form.password){
                this.errors.password = 'password dibutuhkan'
            }else if(!this.isValidpassword(this.form.password)){
                this.errors.password = 'password tidak valid'
            }

            return Object.keys(this.errors).length === 0
        },
        
        isValidEmail(email){
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
        },

        async handleSubmit(){
            if(!this.validateForm()) return
            
            try{
                await this.$http.post('/register', this.form)
                this.$router.push('/success')
            }catch (error) {
                this.errors.submit = error
            }
        }
    }
}
</script>